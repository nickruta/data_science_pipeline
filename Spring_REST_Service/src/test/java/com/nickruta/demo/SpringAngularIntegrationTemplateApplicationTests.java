package com.nickruta.demo;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
//@SpringBootTest
public class SpringAngularIntegrationTemplateApplicationTests {

    @MockBean
    private MongoTemplate mongoTemplate;
    
	@Test
	public void contextLoads() {
	}

}
