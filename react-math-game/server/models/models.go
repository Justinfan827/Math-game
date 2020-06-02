package models

import (
	"go.mongodb.org/mongo-driver/bson/primitive"
)

type User struct {
	ID   primitive.ObjectID `bson:"_id,omitempty"`
	Name string             `bson: "name"`
}

type Room struct {
	ID       primitive.ObjectID `bson:"_id,omitempty"`
	OwnerID  primitive.ObjectID `bson: "name"`
	Users    []*User            `bson:",omitempty"`
	Question string             `bson: "question"`
	Answer   int64              `bson: "answer"`
	NumLeft  int                `bson: "numleft"`
}
