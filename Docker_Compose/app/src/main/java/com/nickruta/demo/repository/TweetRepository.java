package com.nickruta.demo.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.nickruta.demo.model.Tweet;


@CrossOrigin(origins = "http://localhost:4200")
public interface TweetRepository extends MongoRepository<Tweet, String> {

    public Tweet findById(Long id);
    public static List<Tweet> findByRetweeted(List<Tweet> tweets) {
		return null;
	}

}
