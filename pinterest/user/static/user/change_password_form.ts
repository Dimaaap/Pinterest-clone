//import {useForm, SubmitHandler, SubmitErrorHandler} from "react-hook-form";
const {useForm, SubmitHandler, SubmitErrorHandler} = require("react-hook-form");
//import {CSRFToken} from "./dist/js/csrftoken"
const CSRFToken = require("./dist/js/csrftoken");
//import React from "react";
const React = require("react");
//import styles from "./Form.module.css";
const styles = require("./Form.module.css");

interface IChangePasswordForm {
    old_password: string;
    new_password: string;
    repeat_new_password: string;
}

const Form = () => {
    const { register, handleSubmit, 
        formState } = useForm<IChangePasswordForm>({
            mode: 'onBlur'
    })
    const {errors} = formState;
    const submit: SubmitHandler<IChangePasswordForm> = data => {
        console.log(data)
    }

    const error = data => {
        console.log(data);
    }

    const isValidPasswordValue = data => {
        let numValue: number = Number(data);
        let regex: RegExp = /^[a-zA-Z]+$/;
        if (!isNaN(numValue)){
            return `Пароль повинен містити літери і цифри`
        }else if(regex.test(data)){
            return `Пароль повинен містити літери і цифри`
        }
        return true;
    }

    return(
        <form onSubmit={handleSubmit(submit, error)} className={styles.changeForm}>
            <CSRFToken />
            <div className={styles.container}>
                <label className={styles.formLabel}>Ваш старий пароль</label>
                <input type="password" {...register('old_password', {required:{
                    value:true,
                    message:"Це поле обов'язкове для вводу"
                }})}/>
                <div className={styles.formErrors}>
                {errors.old_password && <p>{errors.old_password.message}</p>}
                </div>
            </div>
            <div className={styles.container}>
                <label className={styles.formLabel}>Введіть новий пароль</label>
                <input type="password" {...register('new_password', {required: {
                    value: true,
                    message: "Це поле обов'язкове"
                }})}/>
                <div className={styles.formErrors}>
                {errors.new_password && <p>{errors.new_password.message}</p>}
                </div>
            </div>
            <div className={styles.container}>
                <label className={styles.formLabel}>Повторіть новий пароль</label>
                <input type="password" {...register('repeat_new_password', 
                {required: {
                    value: true,
                    message: "Це поле обов'язкове"
                }, validate: isValidPasswordValue})} 
                aria-invalid={errors.repeat_new_password ? true: false}/>
                <div className={styles.formErrors}>
                    {errors.repeat_new_password && <p>{errors.repeat_new_password.message}</p>}
                </div>
            </div>
            <button type="submit" className={styles.btn}>Зміна паролю</button>
        </form>
    )
}

ReactDOM.render(<Form />, document.getElementById('registration_form'));

export default Form