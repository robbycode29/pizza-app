import axios from "axios";

const base_url = "https://8aaa-85-186-24-110.eu.ngrok.io/";

export default {
    login: async (userData) => {
        const response = await axios.post(base_url + "login/", {
            mothod: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            username: userData.username,
            password: userData.password,
        });
        return response.data;
    }
}

