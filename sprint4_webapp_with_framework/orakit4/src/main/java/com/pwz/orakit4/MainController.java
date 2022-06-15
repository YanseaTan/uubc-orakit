package com.pwz.orakit4;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//@Controller
@RestController
public class MainController {

    @RequestMapping("/")
    public String root(){
        System.out.println("root()");
        return "redirect:index.html";
    }

    @RequestMapping("/chat")
    public String chat() {
        System.out.println("chat()");
        return "default response from chatbot";
    }

}
