package com.itbaizhan.action;

import static org.junit.Assert.*;

import org.junit.Test;

public class UserActionTest2 {
	UserAction user = new UserAction();

	@Test
	public void testCase1() {
		assertEquals("用户名不能为空!",user.register(""));
	}
	@Test
	public void testCase2() {
		assertEquals("用户名已存在!",user.register("admin"));
	}
	@Test
	public void testCase3() {
		assertEquals("注册成功, 请登录!",user.register("lisi"));
	}


}
