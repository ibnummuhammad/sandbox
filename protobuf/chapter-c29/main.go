package main

import (
	"fmt"
	"os"

	"google.golang.org/protobuf/encoding/protojson"

	"chapter-c29/model"
)

func main() {
	var user1 = &model.User{
		Id: "u001",
		Name: "Sylvana Windrunner",
		Password: "f0r Th3 H0rd3",
		Gender: model.UserGender_FEMALE,
	}

	// var userList = &model.UserList{
	// 	List: []*model.User{
	// 		user1,
	// 	},
	// }

	var garage1 = &model.Garage{
		Id: "g001",
		Name: "Kalimdor",
		Coordinate: &model.GarageCoordinate{
			Latitude: 23.2212847,
			Longitude: 53.22033123,
		},
	}

	var garageList = &model.GarageList{
		List: []*model.Garage{
			garage1,
		},
	}

	// var garageListByUser = &model.GarageListByUser{
	// 	List: map[string]*model.GarageList{
	// 		user1.Id: garageList,
	// 	},
	// }

	fmt.Printf("# ==== Original\n       %#v \n", user1)
	fmt.Printf("# ==== As String\n       %s \n", user1.String())

	jsonb, err1 := protojson.Marshal(garageList)
	if err1 != nil {
		fmt.Println(err1.Error())
		os.Exit(0)
	}
	fmt.Printf("# ==== As JSON String\n       %s \n", string(jsonb))
}
