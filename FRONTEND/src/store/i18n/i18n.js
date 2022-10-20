import { defineStore } from "pinia";

export const i18nStore = defineStore('i18nStore',{
    state:()=>({
        locale:'es'
    }),
    getters:{
        getLocale(state){
            return state.locale
        }
    },
    actions:{
        setLocal(value){
            this.locale = value
        }
    }
})