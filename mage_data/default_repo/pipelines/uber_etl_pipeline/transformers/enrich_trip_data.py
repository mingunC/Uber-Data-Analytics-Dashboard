from pyspark.sql import functions as F
from pyspark.sql.window import Window


@transformer
def enrich_trip_data(df, *args, **kwargs):
    """
    Enrich Uber trip data with additional features
    """
    # 시간대 카테고리 생성 (아침, 오후, 저녁, 밤)
    time_categories = F.when(F.col("pickup_hour").between(6, 10), "Morning") \
        .when(F.col("pickup_hour").between(11, 15), "Afternoon") \
        .when(F.col("pickup_hour").between(16, 20), "Evening") \
        .otherwise("Night")

    df = df.withColumn("time_of_day", time_categories)

    # 요일 카테고리 생성 (주중/주말)
    df = df.withColumn(
        "day_type",
        F.when(F.col("pickup_day").isin([1, 7]), "Weekend").otherwise("Weekday")
    )

    # 거리 기반 요금 추정 (실제로는 거리 정보가 있어야 함)
    if "trip_distance" in df.columns:
        df = df.withColumn("estimated_fare", F.col("trip_distance") * 2.5 + 3.0)

    # 각 시간대별 평균 승객 수 계산
    window_spec = Window.partitionBy("pickup_hour")
    df = df.withColumn(
        "avg_passengers_per_hour",
        F.avg("passenger_count").over(window_spec)
    )

    # 승객 수 카테고리 생성
    passenger_categories = F.when(F.col("passenger_count") == 1, "Single") \
        .when(F.col("passenger_count").between(2, 3), "Small_Group") \
        .otherwise("Large_Group")

    df = df.withColumn("passenger_group", passenger_categories)

    print(f"데이터 강화 완료: {df.count()} 행")
    return df