from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import TimestampType


@transformer
def clean_trip_data(df, *args, **kwargs):
    """
    Clean and prepare Uber trip data
    """
    # NULL 값 처리
    df = df.na.drop(subset=["pickup_datetime", "dropoff_datetime", "passenger_count"])

    # 데이터 타입 변환
    df = df.withColumn("pickup_datetime", F.col("pickup_datetime").cast(TimestampType()))
    df = df.withColumn("dropoff_datetime", F.col("dropoff_datetime").cast(TimestampType()))

    # 시간 관련 특성 추출
    df = df.withColumn("pickup_hour", F.hour("pickup_datetime"))
    df = df.withColumn("pickup_day", F.dayofweek("pickup_datetime"))
    df = df.withColumn("pickup_month", F.month("pickup_datetime"))

    # 승차 시간 계산 (분 단위)
    df = df.withColumn(
        "trip_duration_minutes",
        F.round(F.col("dropoff_datetime").cast("long") - F.col("pickup_datetime").cast("long")) / 60
    )

    # 이상치 제거 (비정상적으로 짧거나 긴 승차 시간)
    df = df.filter((F.col("trip_duration_minutes") > 1) & (F.col("trip_duration_minutes") < 180))

    # 중복 데이터 제거
    df = df.dropDuplicates()

    print(f"데이터 정제 완료: {df.count()} 행")
    return df