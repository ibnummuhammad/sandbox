import "google/protobuf/empty.proto";

service Users {
	rpc Register(User) returns (google.protobuf.Empty) {}
	rpc List(google.protobuf.Empty) returns (UserList) {}
}
