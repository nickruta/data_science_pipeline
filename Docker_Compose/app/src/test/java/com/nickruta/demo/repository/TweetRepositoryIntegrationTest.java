package com.nickruta.demo.repository;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Example;
import org.springframework.test.context.junit4.SpringRunner;

import com.nickruta.demo.model.Tweet;
import java.util.Optional;
import static org.assertj.core.api.Assertions.assertThat;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TweetRepositoryIntegrationTest {

    @Autowired
    private TweetRepository repository;

    Long test_long = new Long(42424242);
    
    @Before
    public void init() {

        repository.deleteAll();
        repository.save(new Tweet("1", "none", false, "none", "none",
        		"none", "none", "none", "none", "none", test_long,
    			"none", false, "none", "none","none", test_long, 
    			"none", "none", "Sun Sep 22 01:21:26 +0000 2019","none", true, "none", "none", "none", true, "none", 
    			"none", "none","none", "none", "none", "none"));
    }

    @Test
    public void countOneTweet() {

        Example<Tweet> example = Example.of(new Tweet("1", "none", false, "none", "none",
        		"none", "none", "none", "none", "none", test_long,
    			"none", false, "none", "none","none", test_long, 
    			"none", "none", "Sun Sep 22 01:21:26 +0000 2019","none", true, "none", "none", "none", true, "none", 
    			"none", "none","none", "none", "none", "none"));

        assertThat(repository.count(example)).isEqualTo(1L);
    }

    @Test
    public void setsIdOnSave() {

        Tweet tweet = repository.save(new Tweet("1", "none", false, "none", "none",
        		"none", "none", "none", "none", "none", test_long,
    			"none", false, "none", "none","none", test_long, 
    			"none", "none", "Sun Sep 22 01:21:26 +0000 2019","none", true, "none", "none", "none", true, "none", 
    			"none", "none","none", "none", "none", "none"));
        assertThat(tweet.getId()).isNotNull();
    }

    @Test
    public void findOneTweet() {

        Example<Tweet> example = Example.of(new Tweet("1", "none", false, "none", "none",
        		"none", "none", "none", "none", "none", test_long,
    			"none", false, "none", "none","none", test_long, 
    			"none", "none", "Sun Sep 22 01:21:26 +0000 2019","none", true, "none", "none", "none", true, "none", 
    			"none", "none","none", "none", "none", "none"));

        Optional<Tweet> country = repository.findOne(example);
        assertThat(country.get().getId()).isEqualTo(test_long);
    }
}