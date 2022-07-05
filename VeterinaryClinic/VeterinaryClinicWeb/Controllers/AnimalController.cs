using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Extensions;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class AnimalController : Controller
    {
        private readonly IAnimalRepository _animalRepository;
        private readonly IRaceRepository _raceRepository;
        private readonly IAnimalResponsibleRepository _animalResponsibleRepository;

        public AnimalController(IAnimalRepository animalRepository, IRaceRepository raceRepository, IAnimalResponsibleRepository animalResponsibleRepository)
        {
            _animalRepository = animalRepository;
            _animalResponsibleRepository = animalResponsibleRepository;
            _raceRepository = raceRepository;
        }

        // GET: Animal
        public async Task<IActionResult> Index() =>
            View(await _animalRepository.GetAll());


        // GET: Animal/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _animalRepository.GetById(id) is Animal animal)
                return View(animal);

            return NotFound();
        }

        // GET: Animal/Create
        public async Task<IActionResult> Create()
        {
            ViewData["RaceId"] = new SelectList(await _raceRepository.GetAll(), "Id", "Name");
            ViewData["AnimalResponsibleId"] = new SelectList(await _animalResponsibleRepository.GetAll(), "Id", "Name");
            ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>();
            return View();
        }

        // POST: Animal/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,RaceId,Color,Weight,Height,Gender,AnimalResponsibleId")] Animal animal)
        {
            ModelState.Remove(nameof(Animal.Race));
            ModelState.Remove(nameof(Animal.Responsible));
            if (ModelState.IsValid)
            {
                await _animalRepository.Add(animal);
                return RedirectToAction(nameof(Index));
            }
            ViewData["RaceId"] = new SelectList(await _raceRepository.GetAll(), "Id", "Name");
            ViewData["AnimalResponsibleId"] = new SelectList(await _animalResponsibleRepository.GetAll(), "Id", "Name");
            return View(animal);
        }

        // GET: Animal/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _animalRepository.GetById(id) is Animal animal)
            {
                ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>(animal.Gender);
                ViewData["RaceId"] = new SelectList(await _raceRepository.GetAll(), "Id", "Name");
                ViewData["AnimalResponsibleId"] = new SelectList(await _animalResponsibleRepository.GetAll(), "Id", "Name");
                return View(animal);
            }
            return NotFound();
        }

        // POST: Animal/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,RaceId,Color,Weight,Height,Gender,AnimalResponsibleId")] Animal animal)
        {
            if (id != animal.Id)
                return NotFound();

            ModelState.Remove(nameof(Animal.Race));
            ModelState.Remove(nameof(Animal.Responsible));
            if (ModelState.IsValid)
            {
                try
                {
                    await _animalRepository.Update(animal);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }

            ViewData["RaceId"] = new SelectList(await _raceRepository.GetAll(), "Id", "Name");
            ViewData["AnimalResponsibleId"] = new SelectList(await _animalResponsibleRepository.GetAll(), "Id", "Name");
            return View(animal);
        }

        // GET: Animal/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _animalRepository.GetById(id) is Animal animal)
                return View(animal);

            return NotFound();
        }

        // POST: Animal/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _animalRepository.GetById(id) is Animal animal)
                await _animalRepository.Delete(animal);

            return RedirectToAction(nameof(Index));
        }
    }
}
