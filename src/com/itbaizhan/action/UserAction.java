package com.itbaizhan.action;

import javax.annotation.Resource;

import org.apache.struts2.convention.annotation.Action;
import org.apache.struts2.convention.annotation.Namespace;
import org.apache.struts2.convention.annotation.Result;
import org.apache.struts2.convention.annotation.Results;

import com.itbaizhan.entity.Users;
import com.itbaizhan.service.UserService;

@Action("user")
@Namespace("/index")
@Results({
	@Result(name="login",location="/index/login.jsp"),
	@Result(name="register",location="/index/register.jsp"),
	@Result(name="index",location="index.action",type="redirect"),
})
public class UserAction extends BaseAction{
	private static final long serialVersionUID = 1L;
	
	private Users user;
	 String username="admin";
	
	@Resource
	private UserService userService;

	
	/**
	 * 注册用户
	 * @return
	 */
	public String register(String username){
		if (username.isEmpty()) {
			addActionMessage("用户名不能为空!");
			return "用户名不能为空!";
		}else if (username.equals(username)) {
			addActionMessage("用户名已存在!");
			return "用户名已存在!";
		}else {
			userService.add(user);
			addActionMessage("注册成功, 请登录!");
			return "注册成功, 请登录!";
		}
	}
	
	/**
	 * 用户登录
	 * @return
	 * @throws Exception
	 */
	public String login() {
		if(userService.checkUser(user.getUsername(), user.getPassword())){
			getSession().put("username", user.getUsername());
			return "index";
		} else {
			addActionMessage("用户名或密码错误!");
			return "login";
		}
	}

	/**
	 * 注销登录
	 * @return
	 */
	public String logout() {
		getSession().remove("username");
		getSession().remove("indent");
		return "login";
	}
	
	
	
	public Users getUser() {
		return user;
	}

	public void setUser(Users user) {
		this.user = user;
	}

	
}
