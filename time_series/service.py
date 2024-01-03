from snet.sdk import SnetSDK
import config
import time_series_forecast_pb2
import time_series_forecast_pb2_grpc

def invoke_service():
   snet_config = {
      "private_key": config.PRIVATE_KEY,
      "eth_rpc_endpoint": config.ETH_RPC_ENDPOINT,
      "free_call_auth_token-bin": config.FREE_CALL_AUTH_TOKEN_BIN,
      "free-call-token-expiry-block": config.FREE_CALL_TOKEN_EXPIRY_BLOCK,
      "email": config.EMAIL
   }
   sdk = SnetSDK(config=snet_config)
   service_client = sdk.create_service_client(
      org_id=config.ORG_ID,
      service_id=config.SERVICE_ID,
      service_stub= time_series_forecast_pb2_grpc.ForecastStub # replace service_stub
   )
   request = time_series_forecast_pb2.Input(
      window_len = 15,
      word_len = 7,
      alphabet_size = 5,
      source_type = "csv",
      source = "https://drive.google.com/file/d/1mV73y-SrBzRZS6FuCzBhyrotZhx0mwPo/view?usp=sharing",
      contract = "",
      start_date = "",
      end_date = ""
   ) # replace input_method and arguments
   response = service_client.service.forecast(request) # replace service_method
   print(f"service invoked successfully :: response :: {response}")


invoke_service() # call invoke service method