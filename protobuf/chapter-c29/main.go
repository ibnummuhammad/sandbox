package main

import (
	"fmt"
	"os"

	"chapter-c29/model"
)

func main() {
	var user1 = &model.User{
		id: "u001",
		Name: "Sylvana Windrunner",
		Password: "f0r Th3 H0rd3",
		Gender: model.UserGender_FEMALE,
	}

	var userList = &model.UserList{
		List: []*model.User{
			user1,
		},
	}

	var garage1 = &model.Garage{
		Id: "g001",
		Name: "Kalimdor",
		Coordinate: &model.GarageCoordinate{
			Latitude: 23.2212847,
			Longitude: 53.22033123,
		},
	}
}
