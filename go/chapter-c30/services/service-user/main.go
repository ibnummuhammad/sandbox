package main

import (
	"context"
	"log"
	"net"

	"chapter-c30/common/config"
	"chapter-c30/common/model"

	"google.golang.org/protobuf/types/known/emptypb"
	"google.golang.org/grpc"
)

var localStorage * model.UserList

func init() {
	localStorage = new(model.UserList)
	localStorage.List = make([]*model.User, 0)
}
