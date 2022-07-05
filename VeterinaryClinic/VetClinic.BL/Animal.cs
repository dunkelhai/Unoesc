using System.ComponentModel.DataAnnotations;
using System.Globalization;

namespace VeterinaryClinic.BL
{
    public class Animal : IRegistroBancoDados
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int RaceId { get; set; }
        public Race Race { get; set; }
        public string Color { get; set; }

        [DisplayFormat(DataFormatString = "{0:0.000}")]
        public decimal Weight { get; set; }

        [DisplayFormat(DataFormatString = "{0:0.00}")]
        public decimal Height { get; set; }
        public Gender Gender { get; set; }
        public int AnimalResponsibleId { get; set; }

        [Display(Name = "Responsible")]
        public AnimalResponsible Responsible { get; set; }

        public Animal()
        {
        }

        public Animal(int id, string name, int raceId, Race race, string color, decimal weight, decimal height, Gender gender, int animalResponsibleId, AnimalResponsible responsible)
        {
            Id = id;
            Name = name;
            RaceId = raceId;
            Race = race;
            Color = color;
            Weight = weight;
            Height = height;
            Gender = gender;
            AnimalResponsibleId = animalResponsibleId;
            Responsible = responsible;
        }

        public bool Validate()
        {
            bool isValid = true;

            if (string.IsNullOrEmpty(Name)) isValid = false;
            if (string.IsNullOrEmpty(Color)) isValid = false;

            return isValid;
        }
    }
}
