import axios from "axios";
import base_url from "./base_url";

const url = base_url

export default {
    login: async (userData) => {
        const response = await axios.post(url + "login/", {
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

