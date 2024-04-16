package main

import (
	"context"
	"fmt"
	"log"
	"strings"

	"chapter-c30/common/config"
	"chapter-c30/common/model"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
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
	user2 := model.User{
		Id: "n002",
		Name: "Nabila Rozan",
		Password: "PasswordTralala",
		Gender: model.UserGender(model.UserGender_value["FEMALE"]),
	}

	user := serviceUser()

	fmt.Printf("\n %s> user test\n", strings.Repeat("=", 10))

	user.Register(context.Background(), &user1)

	user.Register(context.Background(), &user2)
}
