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

type UsersServer struct {
	model.UnimplementedUsersServer
}

func (UsersServer) Register(_ context.Context, param *model.User) (*emptypb.Empty, error) {
	user := param

	localStorage.List = append(localStorage.List, user)

	log.Println("Registring user", user.String())

	return new(emptypb.Empty), nil
}

func (UsersServer) List(context.Context, *emptypb.Empty) (*model.UserList, error) {
	return localStorage, nil
}
