package com.example.demo.controller.com;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("tttransferController")
@RequestMapping("/com/transfer")
public class TransferController {

	@PostMapping()
	public String transfer() {
		return "transfer";
	}
	
}