namespace VeterinaryClinic.BL
{
    public class Specie : IRegistroBancoDados
    {
        public int Id { get; set; }

        public string Name { get; set; }

        //public ICollection<Race> Races { get; set; }

        public Specie()
        {
        }

        public Specie(int id, string name)
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
