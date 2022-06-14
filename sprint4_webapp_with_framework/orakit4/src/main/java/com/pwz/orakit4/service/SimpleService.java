package com.pwz.orakit4.service;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

public interface SimpleService {

    @RequestMapping("/try")
    public String firstTry();
}
