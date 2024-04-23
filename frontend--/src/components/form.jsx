import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';


const LoginForm = () => {
    const formik = useFormik({
      initialValues: {
        username: '',
        password: '',
      },
      validationSchema: Yup.object({
        username: Yup.string().required('Username is required'),
        password: Yup.string().required('Password is required'),
      }),
      onSubmit: (values) => {
        
      },
    });
    return (
      <div>
        <form onSubmit={formik.handleSubmit}>
          {}
        </form>
      </div>
    );
  };
  export default LoginForm;