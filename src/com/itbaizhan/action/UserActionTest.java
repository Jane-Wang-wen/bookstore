package com.itbaizhan.action;

import static org.junit.Assert.*;
import java.util. Scanner;

import org.junit.Test;

public class UserActionTest {

	@Test
	public void testRegister() {
		Scanner sc =new Scanner (System.in) ;
		System.out.println("请输入用户名username:");
		String username = sc.next(); 
		System.out.println("系统是否有用户veck,输入1代表有，输入0代表无");
			int A=sc.nextInt ();
		if(A==1){
			System.out.println("用户名已存在，请重新输入");
			System.exit(0);
		}
		else{
			System.out.println("请输入密码pw");
			String pw = sc.next();
			if(pw.length()<6) {
				System.out.println("密码长度需要大于6位，请重新输入");
			}
			else {
				System.out.println("请输入密码copw");
				String copw = sc.next(); 
				if(!pw.equals(copw)){
					System.out.println("密码与确认密码不一致，请重新输入");
				}
				else
					System.out.println("用户新增成功");
			}
			
}
	}

}
