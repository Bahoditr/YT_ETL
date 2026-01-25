from airflow.decorators import dag, task
from datetime import datetime
from airflow.models import Variable

#load_dotenv(dotenv_path='./.env', override = True)
#API_KEY = os.getenv("API_KEY")
#CHANNEL_HANDLE = 'CHANNEL_HANDLE'
API_KEY = Variable.get("API_KEY")
CHANNEL_HANDLE = Variable.get("CHANNEL_HANDLE")

@dag(
    dag_id="zzz_simple_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
)
def zzz_simple_test_dag():

    @task
    def hello():
        print(API_KEY)

    hello()

zzz_simple_test_dag()
