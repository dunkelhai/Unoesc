using System.ComponentModel.DataAnnotations;

namespace VeterinaryClinic.BL
{
    public class Person : IRegistroBancoDados
    {
        public int Id { get; set; }

        public string Name { get; set; }

        public string CPF { get; set; }

        [Display(Name = "E-mail")]
        public string Email { get; set; }

        public string Phone { get; set; }

        public Gender Gender { get; set; }

        public Person()
        {
        }

        public Person(int id, string name, string cpf, string email, string phone, Gender gender)
        {
            Id = id;
            Name = name;
            CPF = cpf;
            Email = email;
            Phone = phone;
            Gender = gender;
        }

        public bool Validate()
        {
            bool isValid = true;

            if (string.IsNullOrEmpty(Name)) isValid = false;
            if (string.IsNullOrEmpty(Email)) isValid = false;
            if(string.IsNullOrEmpty(Phone)) isValid = false;

            return isValid;
        }
    }
}

