import { createI18n } from 'vue-i18n'
import en from './locales/en'
import es from './locales/es'
import { i18nStore } from '@/store/i18n/i18n'


const messages = {
    en,
    es
}

export function installI18n(app) {
    const i18n = createI18n({
        locale:i18nStore().getLocale ,
        fallbackLocale: 'en',
        messages,
        // legacy:false //En false deja usar el i18n en el script, pero no deja cambiar el idioma con el store.
      })
    app.use(i18n);
    return i18n;
  }