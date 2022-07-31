import api from "../../api/auth";

const state = {
    username: "",
    password: "",
    access: "",
    refresh: "",
}

const getters = {
    getUsername: state => state.username,
    getPassword: state => state.password,
    getAccess: state => state.access,
    getRefresh: state => state.refresh,
}

const actions = {
    login({ commit }, userData) {
        commit("setUsername", userData.username);
        commit("setPassword", userData.password);

        let response = api.login(userData);
        response.then(response => {
            commit("setAccess", response.access);
            commit("setRefresh", response.refresh);
        }).catch(error => {
            console.log(error);
        });
    }
}

const mutations = { 
    setPassword: (state, password) => state.password = password, 
    setUsername: (state, username) => state.username = username,
    setAccess: (state, access) => state.access = access,
    setRefresh: (state, refresh) => state.refresh = refresh,
}

export default {
    state,
    getters,
    actions,
    mutations
}