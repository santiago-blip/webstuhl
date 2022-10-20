import { defineStore } from 'pinia'

export const useStorePositionsDetails = defineStore('storePositions', {
  state: () => {
    return { 
      profession: [//
        {id: 1, name: 'Bachillerato'},
        {id: 2, name: 'Técnica'},
        {id: 3, name: 'Tecnología'},
        {id: 4, name: 'Profesional'},
        {id: 5, name: 'Especialización'},
        {id: 6, name: 'Maestría'},
        {id: 7, name: 'Otro'}],
      internal_contacts : [//
        {id: 1, name: 'Estudiantes'},
        {id: 2, name: 'Staff Academico'},
        {id: 3, name: 'Padres de familia'},
        {id: 4, name: 'Staff Administrativo'},
        {id: 5, name: 'Otros'}
      ],
      external_contacts : [//
        {id: 1, name: 'Psicológos'},
        {id: 2, name: 'Psiquiatras'},
        {id: 3, name: 'Neurológos'},
        {id: 4, name: 'Proveedores'},
        {id: 6, name: 'Otros'}
      ],
      relations_objetives : [//
        {id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'},
        {id: 2, description: 'Brindar capacitaciones.'},
        {id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'},
        {id: 4, description: 'Otros'}
      ],
      area : [//
        {id: 1, name: 'Financiera'},
        {id: 2, name: 'Compras'},
        {id: 3, name: 'Tecnología'},
        {id: 4, name: 'Gestión humana'}
      ],
      level : [//
        {id: 1, name: 'Administrativo'},
        {id: 2, name: 'Académico'},
        {id: 3, name: 'Mantenimiento'}
      ],
        positions: [
          {
            id: 'id1', //
            denominacion: 'CONSEJERO ESCUELA PREESCOLAR',
            area:[{id: 1, name: 'Financiera'}], //
            nivel:[{id: 1, name: 'Administrativo'}], //
            active:true,
            dateCreation:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            description: 'Psicólogo especialista en Psicología Educativa, Clinica o Neuro',
            years_of_experience: '3',
            positionImmediateSuperior:'Supervisor del área',
            dateOfEntry:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            aditionalKnowledge:'Experiencia basada en qué',
            competencies:['Capacitado en rescate','Docencia','Maestría gatuna'],
            experience_description: 'años en acompañamientos de procesos educativos',
            languages: 'Nivel avanzado (C1) de inglés', //
            laboralConditions:['Buen ambiente laboral','hard work','be happy'],
            purpose: 'Acompañar y realizar planes y procesos de promoción y prevención que permitan fomentar el bienestar y desarrollo socio emocional de los miembros de la comunidad educativa.',
            responsabilities: [
              'Realizar asesorías psicológicas individuales y grupales con el fin de atender las necesidades socio-emocionales y apoyar algunos procesos académicos de los estudiantes del colegio.',
              'Participar en equipos interdisciplinarios (MDT Equipo multidisciplinario, PAC- Comité de evaluación permanente, Comité de Convivencia Escolar, Reuniones de nivel, Procesos de Admisiones, entre otros) para definir estrategias de acompañamiento dirigidas a estudiantes, familias y miembros del staff.',
              'Acompañar a los directores, profesores y padres de familia en procesos de carácter disciplinario  de los estudiantes.',
              'Liderar capacitaciones, conferencias y actividades de orientación a los miembros de la comunidad educativa enfocados en la promoción y prevención de temas relacionados a la crianza, salud mental y el desarrollo socio-emocional.'
            ],
            internal_relations_contacts: [//
              {id: 1, name: 'Estudiantes'}
            ],
            internal_relations_objetives: [//
              {id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'}
            ],
            external_relations_contacts: [//
              {id: 1, name: 'Psicológos'}
            ],
            external_relations_objetives: [//
              {id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'}
            ],
            academic: [//
              {id: 4, name: 'Profesional', desc: 'Psicología'}
            ]
           },
           {
            id: 'id2',
            denominacion: 'ASISTENTE ADMINISTRATIVO',
            area:[{id: 1, name: 'Financiera'}],
            nivel:[{id: 1, name: 'Administrativo'}],
            active:true,
            dateCreation:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            description: 'Administrador de empresas con experiencia en gestión',
            years_of_experience: '2',
            positionImmediateSuperior:'Supervisor del área',
            dateOfEntry:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            aditionalKnowledge:'Experiencia basada en qué',
            competencies:['Capacitado en rescate','Docencia','Maestría gatuna'],
            experience_description: 'años en acompañamientos de procesos administrativos',
            languages: 'Nivel intermedio (A2) de inglés',
            laboralConditions:['Buen ambiente laboral','hard work','be happy'],
            purpose: 'Acompañar y realizar planes y procesos de promoción y prevención que permitan fomentar el bienestar y desarrollo socio emocional de los miembros de la comunidad educativa y administrativa.',
            responsabilities: [
              'Realizar asesorías psicológicas individuales y grupales con el fin de atender las necesidades socio-emocionales y apoyar algunos procesos académicos de los estudiantes del colegio.',
              'Participar en equipos interdisciplinarios (MDT Equipo multidisciplinario, PAC- Comité de evaluación permanente, Comité de Convivencia Escolar, Reuniones de nivel, Procesos de Admisiones, entre otros) para definir estrategias de acompañamiento dirigidas a estudiantes, familias y miembros del staff.',
              'Acompañar a los directores, profesores y padres de familia en procesos de carácter disciplinario  de los estudiantes.',
              'Liderar capacitaciones, conferencias y actividades de orientación a los miembros de la comunidad educativa enfocados en la promoción y prevención de temas relacionados a la crianza, salud mental y el desarrollo socio-emocional.'
            ],
            internal_relations_contacts: [
              {id: 1, name: 'Estudiantes'}
            ],
            internal_relations_objetives: [
              {id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'}
            ],
            external_relations_contacts: [
              {id: 1, name: 'Psicológos'}
            ],
            external_relations_objetives: [
              {id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'}
            ],
            academic: [
              {id: 4, name: 'Profesional', desc: 'Psicología'}
            ]
           },
           {
            id: 'id3',
            denominacion: 'PROFESOR INGLÉS ESCUELA SUPERIOR',
            area:[{id: 1, name: 'Financiera'}],
            nivel:[{id: 1, name: 'Administrativo'}],
            active:true,
            dateCreation:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            description: 'Psicólogo especialista en Psicología Educativa docencia',
            years_of_experience: '2',
            positionImmediateSuperior:'Supervisor del área',
            dateOfEntry:`${new Date().getFullYear()}/${new Date().getMonth()+1}/${new Date().getDate()}`,
            aditionalKnowledge:'Experiencia basada en qué',
            competencies:['Capacitado en rescate','Docencia','Maestría gatuna'],
            experience_description: 'años en acompañamientos de procesos educativos del lenguaje',
            languages: 'Nivel avanzado (C2) de inglés',
            laboralConditions:['Buen ambiente laboral','hard work','be happy'],
            purpose: 'Acompañar y realizar planes y procesos de promoción y prevención que permitan fomentar el bienestar y desarrollo socio emocional de los miembros de la comunidad educativa orientado a ser el mejor en la enseñanza del idioma.',
            responsabilities: [
              'Realizar asesorías psicológicas individuales y grupales con el fin de atender las necesidades socio-emocionales y apoyar algunos procesos académicos de los estudiantes del colegio.',
              'Participar en equipos interdisciplinarios (MDT Equipo multidisciplinario, PAC- Comité de evaluación permanente, Comité de Convivencia Escolar, Reuniones de nivel, Procesos de Admisiones, entre otros) para definir estrategias de acompañamiento dirigidas a estudiantes, familias y miembros del staff.',
              'Acompañar a los directores, profesores y padres de familia en procesos de carácter disciplinario  de los estudiantes.',
              'Liderar capacitaciones, conferencias y actividades de orientación a los miembros de la comunidad educativa enfocados en la promoción y prevención de temas relacionados a la crianza, salud mental y el desarrollo socio-emocional.'
            ],
            internal_relations_contacts: [
              {id: 1, name: 'Estudiantes'}
            ],
            internal_relations_objetives: [
              {id: 1, description: 'Brindar apoyo en procesos acádemicos y psicológicos.'}
            ],
            external_relations_contacts: [
              {id: 1, name: 'Psicológos'}
            ],
            external_relations_objetives: [
              {id: 3, description: 'Remitir procesos y mantener comunicación con los especialistas externos con el fin de realizar un trabajo interdisciplinario.'}
            ],
            academic: [
              {id: 4, name: 'Profesional', desc: 'Psicología'}
            ]
           }
        ] 
    }
  },
  actions: {
    addVacancie(newVacancieContent){
      if(!newVacancieContent.id){
        let currentDate = new Date().getTime(),
          id = currentDate.toString()
      newVacancieContent.id = id
      this.positions.push(newVacancieContent)
      }
    },
    deleteVacancie(vacancieToDelete){
      this.positions.splice(this.positions.indexOf(vacancieToDelete),1)
    }
  },
  getters: {
    getPositionsContent: (state) => {
      return (id) => {
        return state.positions.find(position => { return position.id == id})
      }
    }
  }
})

