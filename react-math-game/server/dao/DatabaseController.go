package dao

import (
	"context"
	"fmt"
	"github.com/Justinfan827/Math-game.git/models"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
	"math/rand"
	"os"
	"strconv"
	"time"
)

// Global client variable
var client mongo.Client

const devURI = "mongodb+srv://justin_fan:justin_fan@cluster0-jc1fd.mongodb.net/test?retryWrites=true&w=majority"
const localURI = "mongodb://localhost:27017"

var UserCollection *mongo.Collection
var RoomsCollection *mongo.Collection
var ctx context.Context

func Init() {
	connectionType := os.Args[1]

	var uri string
	if connectionType == "dev" {
		uri = devURI
		fmt.Println("connecting to dev mongo db")
	} else {
		uri = localURI
		fmt.Println("connecting to local mongo db:", localURI)
	}
	client, err := mongo.NewClient(options.Client().ApplyURI(uri))
	if err != nil {
		log.Fatal(err)
	}
	ctx, _ = context.WithTimeout(context.Background(), 10*time.Second)
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}

	quickstartDatabase := client.Database("quickstart")
	UserCollection = quickstartDatabase.Collection("users")
	RoomsCollection = quickstartDatabase.Collection("rooms")

}

func generateQuestion() (question string, answer int64) {
	rand.Seed(time.Now().UnixNano())
	val1 := rand.Int63n(99) + 1
	val2 := rand.Int63n(99) + 1
	valueMap := map[int]string{
		0: "+",
		1: "-",
		2: "*",
		3: "/",
	}
	idx := rand.Intn(4)
	switch idx {
	case 0:
		answer = val1 + val2
	case 1:
		answer = val1 - val2
	case 2:
		answer = val1 * val2
	case 3:
		// enumerate all factors of a numberr
		//answer = val1 / val2
	}
	question = strconv.FormatInt(val1, 10) + valueMap[idx] + strconv.FormatInt(val2, 10)
	return
}

func createRoom(userID primitive.ObjectID, numQuestions int) (models.Room, error) {
	question, answer := generateQuestion()
	fmt.Println("question and answer:", question, answer)
	room := &models.Room{
		ID:       primitive.NewObjectID(),
		OwnerID:  userID,
		Users:    []*models.User{},
		Question: question,
		Answer:   answer,
		NumLeft:  numQuestions,
	}
	res, err := RoomsCollection.InsertOne(ctx, room)
	if err != nil {
		return models.Room{}, err
	}
	room.ID = res.InsertedID.(primitive.ObjectID)
	return *room, nil
}
