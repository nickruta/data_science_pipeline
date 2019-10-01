package com.nickruta.demo;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import com.nickruta.demo.repository.TweetRepository;

@SpringBootApplication
@EnableMongoRepositories(basePackages = {"com.nickruta"})
public class SpringAngularIntegrationTemplateApplication {
	
	public static void main(String[] args) {
		SpringApplication.run(SpringAngularIntegrationTemplateApplication.class, args);
	}
    @Bean
    ApplicationRunner init(TweetRepository tweetRepository) {
        return args -> {  
        	// show a tweet on the console at startup
        	Pageable limit = PageRequest.of(0,1);
            tweetRepository.findAll(limit).forEach(System.out::println);
        };
    }  
}
