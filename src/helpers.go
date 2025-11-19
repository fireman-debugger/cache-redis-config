package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
)

type CacheConfig struct {
	RedisHost     string `json:"redisHost"`
	RedisPort    int    `json:"redisPort"`
	RedisPassword string `json:"redisPassword"`
	RedisUsername string `json:"redisUsername"`
	RedisDatabase int    `json:"redisDatabase"`
}

func loadConfig() (*CacheConfig, error) {
	data, err := ioutil.ReadFile("cache-redis-config.json")
	if err != nil {
		return nil, err
	}
	var config CacheConfig
	err = json.Unmarshal(data, &config)
	return &config, err
}

func main() {
	config, err := loadConfig()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(config)
}