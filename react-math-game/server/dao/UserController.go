package dao

import (
	"context"
	"github.com/Justinfan827/Math-game.git/models"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type UserController struct {
	userCollection *mongo.Collection
	ctx            context.Context
}

func (uc UserController) NewUserController(col *mongo.Collection, ctx context.Context) {
	uc.userCollection = col
	uc.ctx = ctx
}

func (uc UserController) deleteUser(id primitive.ObjectID) (*models.User, error) {
	// Call the DeleteOne() method by passing BSON
	var u models.User
	result := uc.userCollection.FindOneAndDelete(ctx, bson.M{"_id": id}, options.FindOneAndDelete())

	err := result.Decode(&u)
	if err != nil {
		return nil, err
	}
	return &u, nil

}

//func updateUser(id)

// Add a user to monogodb
func (uc UserController) createUser(name string) (*models.User, error) {
	user := &models.User{Name: name, ID: primitive.NewObjectID()}

	res, err := uc.userCollection.InsertOne(ctx, user)
	if err != nil {
		return nil, err
	}
	id := res.InsertedID
	user.ID = id.(primitive.ObjectID)
	return *user, nil
}
