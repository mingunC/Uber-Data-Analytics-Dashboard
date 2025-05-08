from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import pandas as pd
from pyspark.sql import SparkSession


@data_loader
def load_trip_data(*args, **kwargs):
    """
    Load Uber trip data from GCS or local file
    """
    # 설정 파일 로드
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    config = ConfigFileLoader(config_path, config_profile)

    # 로컬에서 데이터 로드 (개발 시 사용)
    try:
        # 로컬 샘플 데이터 먼저 시도
        df = pd.read_csv('../data/sample/trip_data_sample.csv')
        print("로컬 샘플 데이터 로드 성공")
    except:
        # GCS에서 데이터 로드
        print("GCS에서 데이터 로드 시도 중...")
        bucket_name = config.get('GCS', 'BUCKET_NAME')
        object_key = 'raw/trip_data.csv'

        gcs = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile))
        df = gcs.load(bucket_name, object_key)

    # Spark 세션 생성 및 데이터프레임 변환
    spark = SparkSession.builder \
        .appName("UberDataLoad") \
        .master(config.get('PYSPARK', 'MASTER_URL')) \
        .getOrCreate()

    # Pandas DataFrame을 PySpark DataFrame으로 변환
    spark_df = spark.createDataFrame(df)

    print(f"데이터 로드 완료: {spark_df.count()} 행")
    return spark_df