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

func serviceGarage() model.GaragesClient {
	port := config.ServiceGaragePort
	conn, err := grpc.Dial(port, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatal("could not connect to", port, err)
	}

	return model.NewGaragesClient(conn)
}

func serviceUser() model.UsersClient {
	port := config.ServiceUserPort
	conn, err := grpc.Dial(port, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatal("could not connect to", port, err)
	}

	return model.NewUsersClient(conn)
}

func main() {
	user1 := model.User{
		Id: "n001",
		Name: "Noval Agung",
		Password: "kw8d hl12/3m,a",
		Gender: model.UserGender(model.UserGender_value["MALE"]),
	}

	garage1 := model.Garage{
		Id: "q001",
		Name: "Quel'thalas",
		Coordinate: &model.GarageCoordinate{
			Latitude: 45.123123123,
			Longitude: 54.1231313123,
		},
	}

	user := serviceUser()

	fmt.Printf("\n %s> user test\n", strings.Repeat("=", 10))

	user.Register(context.Background(), &user1)

	user.Register(context.Background(), &user2)
}
