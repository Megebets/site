import React, { useState } from "react";

function ProfileForm() {
  const [formData, setFormData] = useState({
    fullName: "",
    age: 30,
    hasParents: true,
    birthdate: "",
    birthplace: "",
    hasChildren: false,
    numberOfDaughters: 0,
    numberOfSons: 0,
    education: "",
    residence: "",
    contactPhone: "",
    trustedPersonPhone: "",
    hasHousing: false,
    wasMarried: false,
    height: 170,
    hasCriminalRecord: false,
    hasBadHabits: false,
    performsNamaz: false,
    clothingPreference: "",
    spouseNationalityImportance: false,
    spouseAgePreference: 30,
    okWithDivorcedSpouse: false,
    willingToRelocate: false,
    agreeToBeSecondWife: false,
    planToHaveChildren: true,
    healthStatus: "",
    additionalInfo: "",
    spouseRequirements: "",
    madhab: "",
    profileCompletionDate: "",
    consentToDataProcessing: false,
    avatar: null,
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value, type, checked, files } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: type === "checkbox" ? checked : files ? files[0] : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  
    const formDataToSend = new FormData();
    for (let key in formData) {
      formDataToSend.append(key, formData[key]);
    }
  
    fetch("/api/profile/", {
      method: "POST",
      headers: {
        "X-CSRFToken": window.csrfToken, // Используем токен из шаблона
      },
      body: formDataToSend,
    })
      .then((response) => {
        if (response.ok) {
          alert("Данные успешно сохранены!");
        } else {
          alert("Ошибка сохранения");
        }
      });
  };
  

  return (
    <form onSubmit={handleSubmit} className="profile-form">
      <div className="profile-form__avatar">
        <label>
          <img
            src={formData.avatar ? URL.createObjectURL(formData.avatar) : "/static/default-avatar.jpg"}
            alt="Аватар"
            className="profile-form__avatar-img"
          />
          <input type="file" name="avatar" accept="image/*" onChange={handleChange} />
        </label>
      </div>

      <div className="profile-form__fields">
        <div className="form-group">
          <label>ФИО</label>
          <input type="text" name="fullName" value={formData.fullName} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Возраст</label>
          <input type="number" name="age" value={formData.age} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Дата рождения</label>
          <input type="date" name="birthdate" value={formData.birthdate} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Место рождения</label>
          <input type="text" name="birthplace" value={formData.birthplace} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Контактный телефон</label>
          <input type="text" name="contactPhone" value={formData.contactPhone} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Телефон доверенного лица</label>
          <input type="text" name="trustedPersonPhone" value={formData.trustedPersonPhone} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Образование</label>
          <input type="text" name="education" value={formData.education} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>О себе</label>
          <textarea name="additionalInfo" value={formData.additionalInfo} onChange={handleChange} className="form-control"></textarea>
        </div>
        <div className="form-group">
          <label>Требования к супругу</label>
          <textarea name="spouseRequirements" value={formData.spouseRequirements} onChange={handleChange} className="form-control"></textarea>
        </div>
        <button type="submit" className="btn btn-primary mt-3">Сохранить</button>
      </div>
    </form>
  );
}

export default ProfileForm;
