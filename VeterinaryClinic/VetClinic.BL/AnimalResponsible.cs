namespace VeterinaryClinic.BL
{
    public class AnimalResponsible : Person
    {
        public AnimalResponsible()
        {
        }

        public AnimalResponsible(int id, string name, string cpf, string email, string phone, Gender gender) : base(id, name, cpf, email, phone, gender)
        {
        }
    }
}
