package com.nickruta.demo;

import java.util.ArrayList;
import java.util.EnumSet;
import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import com.nickruta.demo.model.Role;
import com.nickruta.demo.model.RoleName;
import com.nickruta.demo.model.User;
import com.nickruta.demo.repository.RoleRepository;
import com.nickruta.demo.repository.TweetRepository;
import com.nickruta.demo.repository.UserRepository;

@SpringBootApplication
@EnableMongoRepositories(basePackages = {"com.nickruta"})
public class SpringAngularIntegrationTemplateApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringAngularIntegrationTemplateApplication.class, args);
    }
    @Bean
    ApplicationRunner init(UserRepository userRepository, TweetRepository tweetRepository, RoleRepository roleRepository) {
        return args -> {
            // show a tweet on the console at startup
            Pageable limit = PageRequest.of(0,1);
            tweetRepository.findAll(limit).forEach(System.out::println);

            // insert the roles in the roles table
            for (RoleName r : RoleName.values()) {
                Optional<Role> role_found = roleRepository.findByName(r);

                if (role_found.toString() == "Optional.empty") {
                     System.out.println("INSERTING ROLE: " + r);
                     Role role = new Role(r);
                     roleRepository.save(role);
                }

                // // create an admin user
                // User admin = new User();
                // admin.setName("admin");
                // admin.setUsername("admin");
                // admin.setEmail("admin@admin.com");
                // admin.setPassword("123456789");

                // Role admin_role = new Role();
                // admin_role.setName(RoleName.ROLE_ADMIN);

                // Set<Role> admin_roles = new HashSet<>();
                // admin_roles.add(admin_role);
                // admin.setRoles(admin_roles);

                // userRepository.save(admin);

            }
        };


    }
}
