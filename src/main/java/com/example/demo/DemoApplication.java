package com.example.demo;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		try {
			System.out.println("Application Started!");
			SpringApplication.run(DemoApplication.class, args);
	        } catch (Exception e) {
	            e.printStackTrace();
		}
	}

}
