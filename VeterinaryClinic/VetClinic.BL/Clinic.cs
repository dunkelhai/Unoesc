namespace VeterinaryClinic.BL
{
    public class Clinic : IRegistroBancoDados
    {
        public int Id { get; set; }

        public string Name { get; set; }

        public Clinic()
        {
        }

        public Clinic(int id, string name)
        {
            Id = id;
            Name = name;
        }

        public bool Validate()
        {
            bool isValid = true;

            if (string.IsNullOrEmpty(Name)) isValid = false;

            return isValid;
        }
    }
}