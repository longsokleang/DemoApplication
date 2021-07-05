package com.example.demo.controller.cci;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/transfer")
public class TransferController {

	@PostMapping()
	public String transfer( @RequestBody String value ) {
		return value;
	}
	
}
	