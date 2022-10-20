import { defineStore } from "pinia";

export const userLoginStore = defineStore('userLoginStore',{
    state:()=>({
        userLoginData:{
            username:'admin',
            password:'admin'
        }
    }),
    getters:{
        getUsernameLoginData(state){
            return state.userLoginData.username
        },
        getPasswordLoginData(state){
            return state.userLoginData.password
        }
    },
    actions:{
        setUserLoginData(username,password){
            this.userLoginData.username = username
            this.userLoginData.password = password
        }   
    }
})