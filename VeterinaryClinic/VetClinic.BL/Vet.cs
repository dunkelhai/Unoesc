namespace VeterinaryClinic.BL
{
    public class Vet : Person
    {
        public int CouncilNumber { get; set; }

        public Vet()
        {
        }

        public Vet(int councilNumber)
        {
            CouncilNumber = councilNumber;
        }

        public Vet(int id, string name, string cpf, string email, string phone, Gender gender) : base(id, name, cpf, email, phone, gender)
        {
        }

        public new bool Validate()
        {
            bool isValid = true;
            if(CouncilNumber < 0) isValid = false;
            return isValid;
        }
    }
}
