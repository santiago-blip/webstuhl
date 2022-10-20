import App from './App.vue'
//import './style.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { i18nStore } from '@/store/i18n/i18n'
import { Quasar,Notify } from 'quasar'
import { installI18n } from './i18n';
import router from '@/router/router.js'
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'
// import i18n from '@/i18n/index.js'



const app = createApp(App)
app.use(router)
// .use(i18n)
app.use(createPinia())
app.use(Quasar, {
  plugins: {
    Notify
  }
})
const i18n = installI18n(app);
app.mount('#app')

const store = i18nStore()

store.$subscribe((_, state) => {
  i18n.global.locale = state.locale;
});
