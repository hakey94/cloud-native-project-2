import faker
import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

person_ids = [1, 2, 3, 8, 9]
non_person_ids = [987, 56]

fake = faker.Faker()

def random_number():
    return str(fake.pyfloat(1))

# Send the desired payload to existing and non-existing people
payloads = [location_pb2.LocationMessage(person_id=y, latitude=random_number(), longitude=random_number()) for x in [person_ids, non_person_ids] for y in x]

for location in payloads:
    response = stub.Create(location)
    print(f"Response from gRPC server: {response}")