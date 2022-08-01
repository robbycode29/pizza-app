import api from '../../api/pizzas'
// import store from '../modules/auth'


const state = {
    pizzas: [],
    backup:[],
}

const getters = {
    getPizzas: state => state.pizzas,
    getPizzasBackup: state => state.backup,
}

const actions = {
    fetchPizzas: async ({ commit, rootState }) => {
        api.fetchAll(rootState.auth.access).then(response => {
            commit('setPizzas', response.data)
            commit('setPizzasBackup', response.data)
        }).catch(error => {
            console.log(error)
        })
    },
    modifyPizzas: ({ commit }, pizzas) => {
        commit('setPizzas', pizzas)
    }
}

const mutations = { 
    setPizzas: (state, pizzas) => {
        state.pizzas = pizzas
    },
    setPizzasBackup: (state, pizzas) => {
        state.backup = pizzas
    },
    restorePizzasBackup: (state) => { 
        state.pizzas = state.backup
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}