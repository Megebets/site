import React, { useState } from "react";

function RegistrationForm() {
  const [formData, setFormData] = useState({
    lastName: "",
    firstName: "",
    middleName: "",
    phone: "",
    password: "",
    confirmPassword: "",
  });

  const [errors, setErrors] = useState({});

  const validateField = (name, value) => {
    const newErrors = { ...errors };

    switch (name) {
      case "lastName":
      case "firstName":
      case "middleName":
        if (!value.trim()) {
          newErrors[name] = "Поле не может быть пустым";
        } else {
          delete newErrors[name];
        }
        break;

      case "phone":
        const phoneRegex = /^\+?[0-9]{10,15}$/;
        if (!phoneRegex.test(value)) {
          newErrors[name] = "Введите корректный номер телефона";
        } else {
          delete newErrors[name];
        }
        break;

      case "password":
        if (value.length < 6) {
          newErrors[name] = "Пароль должен содержать не менее 6 символов";
        } else {
          delete newErrors[name];
        }
        break;

      case "confirmPassword":
        if (value !== formData.password) {
          newErrors[name] = "Пароли не совпадают";
        } else {
          delete newErrors[name];
        }
        break;

      default:
        break;
    }

    setErrors(newErrors);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    validateField(name, value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Проверка перед отправкой
    const hasErrors = Object.keys(errors).length > 0;
    if (hasErrors) {
      alert("Исправьте ошибки перед регистрацией");
      return;
    }

    // Отправка данных на сервер
    fetch("/profiles/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Регистрация успешна!");
        } else {
          alert("Ошибка регистрации: " + data.message);
        }
      });
  };

  return (
    <form onSubmit={handleSubmit} className="register-form">
      <div className="form-group">
        <label>Фамилия</label>
        <input
          type="text"
          name="lastName"
          value={formData.lastName}
          onChange={handleChange}
          className={`form-control ${errors.lastName ? "is-invalid" : ""}`}
        />
        {errors.lastName && <div className="invalid-feedback">{errors.lastName}</div>}
      </div>

      <div className="form-group">
        <label>Имя</label>
        <input
          type="text"
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
          className={`form-control ${errors.firstName ? "is-invalid" : ""}`}
        />
        {errors.firstName && <div className="invalid-feedback">{errors.firstName}</div>}
      </div>

      <div className="form-group">
        <label>Отчество</label>
        <input
          type="text"
          name="middleName"
          value={formData.middleName}
          onChange={handleChange}
          className={`form-control ${errors.middleName ? "is-invalid" : ""}`}
        />
        {errors.middleName && <div className="invalid-feedback">{errors.middleName}</div>}
      </div>

      <div className="form-group">
        <label>Телефон</label>
        <input
          type="tel"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          className={`form-control ${errors.phone ? "is-invalid" : ""}`}
        />
        {errors.phone && <div className="invalid-feedback">{errors.phone}</div>}
      </div>

      <div className="form-group">
        <label>Пароль</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          className={`form-control ${errors.password ? "is-invalid" : ""}`}
        />
        {errors.password && <div className="invalid-feedback">{errors.password}</div>}
      </div>

      <div className="form-group">
        <label>Подтверждение пароля</label>
        <input
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
          className={`form-control ${errors.confirmPassword ? "is-invalid" : ""}`}
        />
        {errors.confirmPassword && <div className="invalid-feedback">{errors.confirmPassword}</div>}
      </div>

      <button type="submit" className="btn btn-primary">Зарегистрироваться</button>
    </form>
  );
}

export default RegistrationForm;
