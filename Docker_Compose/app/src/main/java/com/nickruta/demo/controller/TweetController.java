package com.nickruta.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.nickruta.demo.model.Tweet;
import com.nickruta.demo.repository.TweetRepository;

import java.util.Collection;
import java.util.stream.Collectors;

@RestController
public class TweetController {

    private TweetRepository repository;

    public TweetController(TweetRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/tweets")
    @CrossOrigin(origins = "http://localhost:4200")
    public Collection<Tweet> coolTweets() {
        return repository.findAll().stream()
//                .filter(this::isRetweeted)
                .collect(Collectors.toList());
    }

    private boolean isRetweeted(Tweet tweet) {
        return tweet.getRetweeted().equals(true);
    }
}