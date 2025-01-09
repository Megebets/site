import axios from "axios";

// Функция для получения CSRF-токена из cookies
const getCsrfToken = () => {
    const cookies = document.cookie.split("; ");
    for (const cookie of cookies) {
        const [name, value] = cookie.split("=");
        if (name === "csrftoken") {
            return value;
        }
    }
    return "";
};

// Регистрация пользователя
export const registerUser = async (formData) => {
    try {
        const response = await axios.post("/api/register/", formData, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
            },
        });

        if (response.status !== 200) {
            throw new Error("Ошибка регистрации.");
        }

        return response.data;
    } catch (error) {
        console.error("Ошибка в registerUser:", error.message);
        throw error;
    }
};

// Пример функции для получения списка пользователей
export const getUsers = async () => {
    try {
        const response = await axios.get("/api/users/", {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken(),
            },
        });

        return response.data;
    } catch (error) {
        console.error("Ошибка в getUsers:", error.message);
        throw error;
    }
};
