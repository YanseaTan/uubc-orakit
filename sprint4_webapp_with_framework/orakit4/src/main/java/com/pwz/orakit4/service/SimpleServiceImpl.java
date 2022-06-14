package com.pwz.orakit4.service;


import org.springframework.web.bind.annotation.RestController;

@RestController
public class SimpleServiceImpl implements SimpleService{
    @Override
    public String firstTry() {
        System.out.println("hello~");
        return "Hello SpringBoot GetMapping";
    }
}
