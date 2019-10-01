package com.nickruta.demo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.nickruta.demo.model.Tweet;
import com.nickruta.demo.repository.TweetRepository;

//The service layer handles business requirements.

// Notice that the DAO/Repository interface will be referenced from the service:
public class TweetService {
	
	@Autowired
	TweetRepository tweetRepository;
	
	public List<Tweet> getAllRetweeted() {
		List<Tweet> tweets = tweetRepository.findAll();
		return TweetRepository.findByRetweeted(tweets);
	}

	public List<Tweet> getAllTweets() {
		List<Tweet> tweets = tweetRepository.findAll();
		return tweets;
	}
}
