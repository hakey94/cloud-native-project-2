python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto

pip3 install grpc --break-system-packages